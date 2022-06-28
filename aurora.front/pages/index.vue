<template>
  <div>
    <!-- Sidebar -->
    <section id="sidebar">
      <div class="inner">
        <nav>
          <ul>
            <li><a href="#intro">Welcome</a></li>
            <li><a href="#one">Who we are</a></li>
            <li><a href="#two">What we do</a></li>
            <li><a href="#three">Get in touch</a></li>
          </ul>
        </nav>
      </div>
    </section>

    <!-- Wrapper -->
    <div id="wrapper">
      <!-- Intro -->
      <section id="intro" class="wrapper style1 fullscreen fade-up">
        <div class="inner">
          <h1>Aurora Client</h1>
          <p>
            This is the web frontend for the Aurora Project.
          </p>
          <ul class="actions">
            <li><a href="#one" class="button scrolly">Learn more</a></li>
          </ul>
        </div>
      </section>

      <!-- One -->
      <section id="one" class="wrapper style2 spotlights">
        <section>
          <a href="#" class="image"
            ><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.RiNRZRvaTwtw6x1S3ipSFwHaHa%26pid%3DApi&f=1" alt="" data-position="center center"
          /></a>
          <div class="content">
            <div class="inner">
              <h2>Blockchain</h2>
              <p>
                an insight into our blockchain
              </p>
              <ul class="actions">
                <li><nuxt-link to="/blockchain" class="button">Learn more</nuxt-link></li>
              </ul>
            </div>
          </div>
        </section>
        <section>
          <a href="#" class="image"
            ><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F000%2F291%2F162%2Foriginal%2Ftransaction-vector-icon.jpg&f=1&nofb=1" alt="" data-position="top center"
          /></a>
          <div class="content">
            <div class="inner">
              <h2>Transaction</h2>
              <p>
                send coins to other persons
              </p>
              <ul class="actions">
                <li><nuxt-link to="/transaction" class="button">Learn more</nuxt-link></li>
              </ul>
            </div>
          </div>
        </section>
        <section>
          <a href="#" class="image"
            ><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgetdrawings.com%2Ffree-icon%2Fminecraft-pickaxe-icon-66.png&f=1&nofb=1" alt="" data-position="25% 25%"
          /></a>
          <div class="content">
            <div class="inner">
              <h2>Mining</h2>
              <p>
                how to mine coins
              </p>
              <ul class="actions">
                <li><nuxt-link to="/mining" class="button">Learn more</nuxt-link></li>
              </ul>
            </div>
          </div>
        </section>
      </section>

      <!-- Two -->
      <section id="two" class="wrapper style3 fade-up">
        <div class="inner">
          <h2>What we do</h2>
          <p>
            We specially designed this coin for the ASG.
          </p>
          <div class="features">
            <section>
              <span class="icon solid major fa-code"></span>
              <h3>Code</h3>
              <p>
                This project is realized in Python and Node.js.
              </p>
            </section>
            <section>
              <span class="icon solid major fa-lock"></span>
              <h3>Security</h3>
              <p>
                Based on mathematical alogrithms.
              </p>
            </section>
            <section>
              <span class="icon solid major fa-cog"></span>
              <h3>Easy Transactions</h3>
              <p>
                Simple payments.
              </p>
            </section>
            <section>
              <span class="icon solid major fa-desktop"></span>
              <h3>User Interface</h3>
              <p>
                User friendly service.
              </p>
            </section>
            <section>
              <span class="icon solid major fa-link"></span>
              <h3>Blockchain</h3>
              <p>
                Data stored for the infinity.
              </p>
            </section>
            <section>
              <span class="icon major fa-gem"></span>
              <h3>Rewards</h3>
              <p>
                Manus manum lavat.
              </p>
            </section>
          </div>
          <ul class="actions">
            <li><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" class="button">Learn more</a></li>
          </ul>
        </div>
      </section>

      <!-- Three -->
      <section id="three" class="wrapper style1 fade-up">
        <div class="inner">
          <h2>Developed by oc7o aka. 0x70 🐙</h2>
          <div class="split style1">
            <section>
              <ul class="contact">
                <li>
                  <h3>Social</h3>
                  <ul class="icons">
                    <li><a href="https://twitter.com/oc7o_/" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
                    <li><a href="https:/github.com/oc7o/aurora/" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
                  </ul>
                </li>
              </ul>
            </section>
          </div>
        </div>
      </section>
    </div>

    <!-- Footer -->
    <AuroraFooter />
  </div>
</template>

<script>
export default {
  head: {
    script: [
        // {src: require('~/assets/js/jquery.min.js')},
        // {src: '~/assets/js/jquery.scrollex.min.js'},
        // {src: '~/assets/js/jquery.scrolly.min.js'},
        // {src: '~/assets/js/browser.min.js'},
        // {src: '~/assets/js/breakpoints.min.js'},
        // {src: '~/assets/js/util.js'},
        // {src: '~/assets/js/main.js'}
    ],
    // noscript: {
    //     link: [
    //         {rel: "stylesheet", href: "~/assets/css/noscript.css"}
    //     ]
    // }
  },
};
</script>
