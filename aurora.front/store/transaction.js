import { secretbox, randomBytes, sign } from "tweetnacl"
import {
  decodeUTF8,
  encodeUTF8,
  encodeBase64,
  decodeBase64
} from "tweetnacl-util"
import { ToastProgrammatic as Toast } from "buefy"

///////////////
/// CRYPTO ///
/////////////

//   \


//////////////
/// STORE ///
////////////

export const state = () => ({
    transactions: [],
    address_nonce: 0,
    address_balance: 0
})


export const mutations = {
    SET_TRANSACTIONS (state, data) {
        state.transactions = data
    },
    SET_ADDRESS_NONCE (state, data) {
        state.address_nonce = data
    },
    SET_ADDRESS_BALANCE (state, data) {
        state.address_balance = data
    }
}

export const actions = {

    // Building a transaction and sending it to the blockchain
    async createTransaction ({ commit, dispatch }, transaction) {

        // for more infos look at the docs: https://github.com/dchest/tweetnacl-js
        // this is the same proccess as in the Backend
        const from_address_private_hex = Buffer.from(transaction['from_address'], 'hex')
        const from_address_object = sign.keyPair.fromSeed(from_address_private_hex)
        const from_address_public_string = Buffer.from(from_address_object.publicKey).toString('hex')
        const from_address_private_string = Buffer.from(from_address_object.secretKey).toString('hex')

        const addressRequest = await this.$axios.get('address_nonce/' + from_address_public_string)
        const nonce = addressRequest.data

        const message_object = Object.assign({nonce: nonce}, transaction)
        message_object['from_address'] = from_address_public_string
        const message_string = JSON.stringify(message_object)
        const message = Buffer.from(message_string)
        
        const signature = sign.detached(message, from_address_object.secretKey)
        const signature_string = Buffer.from(signature).toString('hex')
        message_object['signature'] = signature_string

        // console.log(from_address_private)
        // console.log(from_address_public_string)
        // console.log(message_object)

        await this.$axios.post('transaction/', message_object)
            .then(() => {
                Toast.open({
                    duration: 1500,
                    message: "Success",
                    position: 'is-bottom',
                    type: 'is-success'
                })
            })
            .catch((error) => {
                console.log(error)
                if (error['response'] || error['response']['data'] || error['response']['data'][0]) {
                    dispatch('error/setErrorMessage', error['response']['data'][0], { root: true })
                } else {
                    dispatch('error/setErrorMessage', "Unknown Error", { root: true })
                }
            })
    },

    // get an address' nonce/balance
    async getAddressStatus ({ commit }, address) {
        const nonceRequest = await this.$axios.get('address_nonce/' + address)
        const balanceRequest = await this.$axios.get('address_balance/' + address)
        commit('SET_ADDRESS_NONCE', nonceRequest.data)
        commit('SET_ADDRESS_BALANCE', balanceRequest.data)
    }
}