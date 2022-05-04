<template>
  <div>
    <!-- Header -->
    <header id="header">
      <nuxt-link to="/" class="title">Aurora</nuxt-link>
      <nav>
        <ul>
          <li><nuxt-link to="/">Home</nuxt-link></li>
          <li><nuxt-link to="/blockchain" class="active">Blockchain</nuxt-link></li>
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
          <h1 class="major">Blockchain</h1>
          <!-- <span class="image fit"
            ><img :src="require('~/assets/images/pic04.jpg')" alt=""
          /></span>
          <p>...</p>
          <p>...</p> -->
          <ul class="tilesWrap">
            <li v-for="block in blocks" :key="block.block_hash">
              <h2>{{ block.pk }}</h2>
              <h3>{{ block.block_hash }}</h3>
              <p>
                Previous Block: {{ block.prev_block }}
              </p>
              <p>
                Nonce: {{ block.nonce }}
              </p>
              <p>
                Transactions Hash: {{ block.transactions_hash }}
              </p>
              <p>
                Transactions Count: {{ block.transaction_counter }}
              </p>
              <button><nuxt-link :to="`/blockchain/${block.block_hash}`">Transactions</nuxt-link></button>
            </li>
          </ul>
        </div>
      </section>
	  <br><br><br><br><br><br>
      <AuroraFooter />
    </div>
  </div>
</template>
<script>
export default {
  async fetch () {
    await this.$store.dispatch('blockchain/getBlockchain')
  },
  computed: {
    blocks () {
	  this.$fetch()
      return this.$store.state.blockchain.blocks
    }
  }
}
</script>
<style>
.tilesWrap {
	padding: 0;
	margin: 50px auto;
	list-style: none;
	text-align: center;
}
.tilesWrap li {
	display: inline-block;
	width: 80%;
	min-width: 800px;
	max-width: 920px;
	padding: 80px 20px 40px;
	position: relative;
	vertical-align: top;
	margin: 10px;
	font-family: 'helvetica', san-serif;
	min-height: 25vh;
	background: #262a2b;
	border: 1px solid #252727;
	text-align: left;
}
.tilesWrap li h2 {
	font-size: 114px;
	margin: 0;
	position: absolute;
	opacity: 0.2;
	top: 50px;
	right: 10px;
	transition: all 0.3s ease-in-out;
}
.tilesWrap li h3 {
	font-size: 20px;
	color: #b7b7b7;
	margin-bottom: 5px;
}
.tilesWrap li p {
	font-size: 16px;
	line-height: 18px;
	color: #b7b7b7;
	margin-top: 5px;
}
.tilesWrap li button {
	background: transparent;
	border: 1px solid #b7b7b7;
	padding: 10px 20px;
	color: #b7b7b7;
	border-radius: 3px;
	position: relative;
	transition: all 0.3s ease-in-out;
	transform: translateY(-40px);
	opacity: 0;
	cursor: pointer;
	overflow: hidden;
  left: 500px;
}
.tilesWrap li button:before {
	content: '';
	position: absolute;
	height: 100%;
	width: 120%;
	background: #b7b7b7;
	top: 0;
	opacity: 0;
	left: -140px;
	border-radius: 0 20px 20px 0;
	z-index: -1;
	transition: all 0.3s ease-in-out;
	
}
.tilesWrap li:hover button {
	transform: translateY(5px);
	opacity: 1;
}
.tilesWrap li button:hover {
	color: #262a2b;
}
.tilesWrap li button:hover:before {
	left: 0;
	opacity: 1;
}
.tilesWrap li:hover h2 {
	top: 0px;
	opacity: 0.6;
}

.tilesWrap li:before {
	content: '';
	position: absolute;
	top: -2px;
	left: -2px;
	right: -2px;
	bottom: -2px;
	z-index: -1;
	background: #fff;
	transform: skew(2deg, 2deg);
}
.tilesWrap li:after {
	content: '';
	position: absolute;
	width: 40%;
	height: 100%;
	left: 0;
	top: 0;
	background: rgba(255, 255, 255, 0.02);
}
.tilesWrap li:nth-child(1):before {
	background: #C9FFBF;
background: -webkit-linear-gradient(to right, #FFAFBD, #C9FFBF);
background: linear-gradient(to right, #FFAFBD, #C9FFBF);
}
.tilesWrap li:nth-child(2):before {
	background: #f2709c;
background: -webkit-linear-gradient(to right, #ff9472, #f2709c);
background: linear-gradient(to right, #ff9472, #f2709c);
}
.tilesWrap li:nth-child(3):before {
	background: #c21500;
background: -webkit-linear-gradient(to right, #ffc500, #c21500);
background: linear-gradient(to right, #ffc500, #c21500);
}
.tilesWrap li:nth-child(4):before {
	background: #FC354C;
background: -webkit-linear-gradient(to right, #0ABFBC, #FC354C);
background: linear-gradient(to right, #0ABFBC, #FC354C);
}
</style>