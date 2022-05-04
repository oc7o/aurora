<template>
  <div>
    <!-- Header -->
    <header id="header">
      <nuxt-link to="/" class="title">Aurora</nuxt-link>
      <nav>
        <ul>
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li>
            <nuxt-link to="/blockchain" class="active">Blockchain</nuxt-link>
          </li>
          <li>
            <nuxt-link to="/transaction">Transaction</nuxt-link>
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
          <h2 class="major">{{ this.$route.params["block"] }}</h2>
          <!-- <span class="image fit"
            ><img :src="require('~/assets/images/pic04.jpg')" alt=""
          /></span>
          <p>...</p>
          <p>...</p> -->
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>From</th>
                  <th>To</th>
                  <th>Amount</th>
                  <th>Fee</th>
                  <th>Hash</th>
                  <th>Nonce</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(transaction, i) in transactions" :key="i">
                  <td>{{ transaction.from_address }}</td>
                  <td>{{ transaction.to_address }}</td>
                  <td>{{ transaction.amount }}</td>
                  <td>{{ transaction.fee }}</td>
                  <td>{{ transaction.transaction_hash }}</td>
                  <td>{{ transaction.nonce }}</td>
                </tr>
              </tbody>
              <!-- <tfoot>
                <tr>
                  <td colspan="2"></td>
                  <td>100.00</td>
                </tr>
              </tfoot> -->
            </table>
          </div>
        </div>
      </section>
      <br><br><br><br><br>
      <AuroraFooter />
    </div>
  </div>
</template>
<script>
export default {
  async fetch() {
    await this.$store.dispatch(
      "blockchain/getBlockTransactions",
      this.$route.params["block"]
    );
  },
  computed: {
    transactions () {
      return this.$store.state.blockchain.transactions;
    },
  },
};
</script>
