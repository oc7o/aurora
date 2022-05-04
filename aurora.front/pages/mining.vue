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
            <nuxt-link to="/transaction">Transaction</nuxt-link>
          </li>
          <li><nuxt-link to="/mining" class="active">Mining</nuxt-link></li>
        </ul>
      </nav>
    </header>

    <!-- Wrapper -->
    <div id="wrapper">
      <!-- Main -->
      <section id="main" class="wrapper">
        <div class="inner">
          <h1 class="major">Mining</h1>
          <span class="image fit"
            ><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F000%2F682%2F501%2Foriginal%2Fmining-for-bitcoins-crypto-currency-concept.jpg&f=1&nofb=1" alt=""
          /></span>
          <h2>Download our Mining Client (only for pros)</h2>
          <p>Replace the data in the file with your credentials.</p>
          <div class="row gtr-uniform">
            <div class="col-6 col-12-xsmall">
              <ul class="actions">
                <li><a href="/main.py" class="button primary" download="">DoWnLoAd (.py)</a></li>
              </ul>
            </div>
          </div>
        </div>
      </section>
      <AuroraFooter />
    </div>
  </div>
</template>

<style scoped>
#mining-pic {
  position: absolute;
  clip: rect(0, 0, 0, 0);
}
</style>