//////////////
/// STORE ///
////////////
import { ToastProgrammatic as Toast } from 'buefy'

export const state = () => ({
    errorMessage: ""
})


export const mutations = {
    SET_ERROR_MESSAGE (state, data) {
        state.errorMessage = data
    }
}

export const actions = {
    // easier for debugging
    async setErrorMessage ({ commit }, errorMessage) {
        commit('SET_ERROR_MESSAGE', errorMessage)
        Toast.open({
            duration: 1500,
            message: errorMessage,
            position: 'is-bottom',
            type: 'is-danger'
        })
    }
}