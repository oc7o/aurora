//////////////
/// STORE ///
////////////

export const state = () => ({
    blocks: [],
    transactions: []
})


export const mutations = {
    SET_BLOCKS (state, data) {
        state.blocks = data
    },
    SET_TRANSACTIONS (state, data) {
        state.transactions = data
    }
}

export const actions = {
    // get ALL Blocks - this could take a while especially if there are many blocks
    async getBlockchain ({ commit }) {
        const request = await this.$axios.get('block/')
            .catch((error) => {
                console.log(error.response)
            })
        commit('SET_BLOCKS', request.data)
    },
    // get all transactions of a specific block
    async getBlockTransactions ({ commit }, block_hash) {
        const request = await this.$axios.get(`transaction/?block=${block_hash}`)
        const requestData = request.data
        commit('SET_TRANSACTIONS', requestData)
    }
}