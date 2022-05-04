<template>
  <div>
    <!-- Header -->
    <header id="header">
      <nuxt-link to="/" class="title">Aurora</nuxt-link>
      <nav>
        <ul>
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li><nuxt-link to="/blockchain">Blockchain</nuxt-link></li>
          <li>
            <nuxt-link to="/transaction" class="active">Transaction</nuxt-link>
          </li>
          <li><nuxt-link to="/mining">Mining</nuxt-link></li>
        </ul>
      </nav>
    </header>

    <!-- Wrapper -->
    <div id="wrapper">
      <!-- Main -->
      <section id="main" class="wrapper">
        <div class="inner">
          <h1 class="major">Transaction</h1>
          <span class="image fit"
            ><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fjelvix.com%2Fwp-content%2Fuploads%2F2018%2F03%2Fblockchain-solutions.jpg&f=1&nofb=1" alt=""
          /></span>
          <h2>Generate a Key Pair</h2>
          <div class="row gtr-uniform">
            <div class="col-6 col-12-xsmall">
              <input
                type="text"
                name="private-key"
                id="private-key"
                placeholder="Your New Private Address"
                v-model="new_pair.private_key"
              />
            </div>
            <br><br>
            <div class="col-6 col-12-xsmall">
              <input
                type="text"
                name="public-key"
                id="public-key"
                placeholder="Your New Public Address"
                v-model="new_pair.public_key"
              />
            </div>
            <br><br>
            <div class="col-12">
              <ul class="actions">
                <li>
                  <input
                    type="submit"
                    value="Generate"
                    class="primary"
                    @click="generateNewKeyPair()"
                  />
                </li>
                <li><input type="reset" value="Clear" @click="clear()" /></li>
              </ul>
            </div>
          </div>
          <br />
          <h2>Send a Transaction</h2>
          <div class="row gtr-uniform">
            <div class="col-6 col-12-xsmall">
              <input
                type="password"
                name="from-private-key"
                id="from-private-key"
                placeholder="Your Private Key"
                v-model="data.from_address"
              />
            </div>
            <div class="col-6 col-12-xsmall">
              <input
                type="text"
                name="to-public-key"
                id="to-public-key"
                placeholder="Receivers Public Address"
                v-model="data.to_address"
              />
            </div>
            <div class="col-6 col-12-xsmall">
              <input
                type="text"
                name="amount"
                id="amount"
                placeholder="Amount"
                v-model="data.amount"
              />
            </div>
            <div class="col-6 col-12-xsmall">
              <input
                type="text"
                name="fee"
                id="fee"
                placeholder="Fee"
                v-model="data.fee"
              />
            </div>
            <div class="col-12">
              <ul class="actions">
                <li>
                  <input
                    type="submit"
                    value="Send Transaction"
                    class="primary"
                    @click="sendTransaction()"
                  />
                </li>
                <li><input type="reset" value="Reset" @click="reset()" /></li>
              </ul>
            </div>
          </div>
          <br />
          <h2>View Address Balance/Nonce</h2>
          <div class="row gtr-uniform">
            <div class="col-6 col-12-xsmall">
              <input
                type="text"
                name="address"
                id="get_address"
                placeholder="address"
                v-model="get_address"
              />
            </div>
            <div class="col-12">
              <ul class="actions">
                <li>
                  <input
                    type="submit"
                    value="Check"
                    class="primary"
                    @click="addressStatus()"
                  />
                </li>
              </ul>
            </div>
            <b-modal v-model="isStatusActive" :width="640" scroll="keep">
              <div class="card">
                <div class="card-content">
                  <br>
                  <p>Address Nonce: {{ address_nonce }}</p>
                  <p>Address Balance: {{ address_balance }}</p>
                </div>
              </div>
            </b-modal>
          </div>
        </div>
      </section>
      <AuroraFooter />
    </div>
  </div>
</template>
<script>
import { ToastProgrammatic as Toast } from "buefy";
import { ModalProgrammatic as Modal } from "buefy";

import { secretbox, randomBytes, sign } from "tweetnacl";

export default {
  data() {
    return {
      data: {
        from_address: "",
        to_address: "",
        amount: 0,
        fee: 0,
      },
      new_pair: {
        private_key: "",
        public_key: "",
      },
      get_address: "",
      isStatusActive: false,
    };
  },
  computed: {
    address_nonce() {
      return this.$store.state.transaction.address_nonce;
    },
    address_balance() {
      return this.$store.state.transaction.address_balance;
    },
  },
  methods: {
    async sendTransaction() {
      if (
        this.data.from_address.length == 64 &&
        (this.data.from_address.length == 32 ||
          this.data.from_address.length == 64) &&
        (this.data.amount > 0 || this.data.fee > 0)
      ) {
        this.data["amount"] = parseInt(this.data["amount"]);
        this.data["fee"] = parseInt(this.data["fee"]);
        await this.$store.dispatch("transaction/createTransaction", this.data);
        this.reset()
      } else {
        Toast.open({
          duration: 1500,
          message: "Invalid input!",
          position: "is-bottom",
          type: "is-danger",
        });
      }
    },
    async generateNewKeyPair() {
      const pair = sign.keyPair();
      const from_address_public_string = Buffer.from(pair.publicKey).toString(
        "hex"
      );
      const from_address_private_string = Buffer.from(pair.secretKey).toString(
        "hex"
      );
      this.new_pair.private_key = from_address_private_string.substring(0,64);
      this.new_pair.public_key = from_address_public_string;
    },
    async reset() {
      this.data = {
        from_address: "",
        to_address: "",
        amount: 0,
        fee: 0,
      };
    },
    async clear() {
      this.new_pair = {
        private_key: "",
        public_key: "",
      };
    },
    async addressStatus() {
      if (this.get_address.length == 64) {
        await this.$store.dispatch(
          "transaction/getAddressStatus",
          this.get_address
        );
        this.isStatusActive = true;
        // Modal.open({
        //   parent: this,
        //   component: this.StatusModal,
        //   hasModalCard: true,
        //   trapFocus: true,
        // });
      } else {
        Toast.open({
          duration: 1500,
          message: "Invalid address!",
          position: "is-bottom",
          type: "is-danger",
        });
      }
    },
  },
};
</script>
