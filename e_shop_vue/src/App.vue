<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Shop</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        
        <div class="navbar-end">
          <router-link to="/breakfast" class="navbar-item">breakfast</router-link>
          <router-link to="/dinner" class="navbar-item">dinner</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>&#xf07a;</span>
                <span class='badge badge-warning' id='lblCartCount'>{{ cartTotalLength }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <header class="header clearfix element_to_stick">
        <div class="layer"></div><!-- Opacity Mask Menu Mobile -->
        <div class="container-fluid">
        <div id="logo">
          <router-link to="/">
            
            <img src="img/logo.svg" width="140" height="35" alt="" class="logo_normal">
            <img src="img/logo_sticky.svg" width="140" height="35" alt="" class="logo_sticky">
        
          </router-link>
            
        </div>
        <ul id="top_menu">
            <li><a href="#0" class="search-overlay-menu-btn"></a></li>
            <li>
                <div class="dropdown dropdown-cart">
                  <router-link to="/cart" class="cart_bt">
                    <strong>{{ cartTotalLength }}</strong>
                  </router-link>

                </div>
                <!-- /dropdown-cart
                  <a href="shop-cart.html" class="cart_bt"><strong>2</strong></a>
                    <div class="dropdown-menu">
                        <ul>
                            <li>
                                <figure><img src="img/item_placeholder_square_small.jpg" data-src="img/item_square_small_1.jpg" alt="" width="50" height="50" class="lazy"></figure>
                                <strong><span>1x Pizza Napoli</span>$12.00</strong>
                                <a href="#0" class="action"><i class="icon_trash_alt"></i></a>
                            </li>
                            <li>
                                <figure><img src="img/item_placeholder_square_small.jpg" data-src="img/item_square_small_2.jpg" alt="" width="50" height="50" class="lazy"></figure>
                                <strong><span>1x Hamburgher Maxi</span>$10.00</strong>
                                <a href="#0" class="action"><i class="icon_trash_alt"></i></a>
                            </li>
                            <li>
                                <figure><img src="img/item_placeholder_square_small.jpg" data-src="img/item_square_small_3.jpg" alt="" width="50" height="50" class="lazy"></figure>
                                <strong><span>1x Red Wine Bottle</span>$20.00</strong>
                                <a href="#0" class="action"><i class="icon_trash_alt"></i></a>
                            </li>
                        </ul>
                        <div class="total_drop">
                            <div class="clearfix add_bottom_15"><strong>Total</strong><span>$32.00</span></div>
                            <a href="shop-cart.html" class="btn_1 outline">View Cart</a><a href="shop-checkout.html" class="btn_1">Checkout</a>
                        </div>
                    </div>
                -->
            </li>
        </ul>
        <!-- /top_menu -->
        <a href="#0" class="open_close">
            <i class="icon_menu"></i><span>Menu</span>
        </a>
        <nav class="main-menu">
            <div id="header_menu">
                <a href="#0" class="open_close">
                    <i class="icon_close"></i><span>Menu</span>
                </a>
                <a href="index.html"><img src="img/logo.svg" width="140" height="35" alt=""></a>
            </div>
            <ul>
                <li class="submenu">
                    <router-link to="/" class="show-submenu">Home</router-link>
                </li>
                <li class="submenu">
                <a href="#0" class="show-submenu">Menu</a>
		            <ul>
                    <li><router-link to="/" class="show-submenu">Menu <span class="badge badge-danger">HOT</span></router-link></li>
		                <li><a href="menu-1.html">Menu 2 Column</a></li>
		                <li><a href="menu-2.html">Menu Add To Cart</a></li>
		                <li><a href="menu-3.html">Menu With Tabs</a></li>
		                <li><a href="menu-4.html">Menu Grid</a></li>
		                <li><a href="menu-of-the-day.html">Menu of the Day <span class="badge badge-danger">HOT</span></a></li>
		                <li><a href="order-food.html">Order Food</a></li>
		                <li><a href="confirm.html">Confirm</a></li>
		            </ul>
                    
                </li>
                <li class="submenu">
                    <router-link to="/" class="show-submenu">Home</router-link>
                </li>
                <li class="submenu">
                    <router-link to="/" class="show-submenu">Home</router-link>
                </li>
                <li class="submenu">
                    <router-link to="/" class="show-submenu">Home</router-link>
                </li>
                <li class="submenu">
                    <router-link to="/" class="show-submenu">Home</router-link>
                </li>

              <template v-if="$store.state.isAuthenticated">
                <li><router-link to="/my-account" class="btn_top">My account</router-link></li>
              </template>

              <template v-else>
                <li><router-link to="/log-in" class="btn_top">Log in</router-link></li>
              </template>
              
            </ul>
        </nav>
      </div>
      <!-- Search -->
      <div class="search-overlay-menu">
          <span class="search-overlay-close"><span class="closebt"><i class="icon_close"></i></span></span>
          <form role="search" id="searchform" method="get">
              <input value="" name="q" type="search" placeholder="Search..." />
              <button type="submit"><i class="icon_search"></i></button>
          </form>
      </div><!-- End Search -->
    </header>

    <section class="section">
      <router-view/>
    </section>

	  <footer>
	    <div class="frame black"></div>
	    <div class="container">
	        <div class="row">
	            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-6">
	                <div class="footer_wp">
	                    <i class="icon_pin_alt"></i>
	                    <h3>Address</h3>
	                    <p>97845 Baker st. 567<br>Los Angeles - US</p>
	                </div>
	            </div>
	            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-6">
	                <div class="footer_wp">
	                    <i class="icon_tag_alt"></i>
	                    <h3>Reservations</h3>
	                    <p><a href="tel:009442323221">+94 423-23-221</a><br><a href="#0">reservations@Foores.com</a></p>
	                </div>
	            </div>
	            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-6">
	                <div class="footer_wp">
	                    <i class="icon_clock_alt"></i>
	                    <h3>Opening Hours</h3>
	                    <ul>
	                        <li>Mon - Sat: 10am - 11pm</li>
	                        <li>Sunday: Closed</li>
	                    </ul>
	                </div>
	            </div>
	            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-6">
	                <h3>Keep in touch</h3>
	                <div id="newsletter">
	                    <div id="message-newsletter"></div>
	                    <form method="post" action="phpmailer/newsletter_template_email.php" name="newsletter_form" id="newsletter_form">
	                        <div class="form-group">
	                            <input type="email" name="email_newsletter" id="email_newsletter" class="form-control" placeholder="Your email">
	                            <button type="submit" id="submit-newsletter"><i class="arrow_carrot-right"></i></button>
	                        </div>
	                    </form>
	                </div>
	            </div>
	        </div>
	        <!-- /row-->
	        <hr>
	        <div class="row">
	            <div class="col-sm-5">
	                <p class="copy">© 2021 Foores Restaurant - All rights reserved</p>
	            </div>
	            <div class="col-sm-7">
	                <div class="follow_us">
	                    <ul>
	                        <li><a href="#0"><img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="img/twitter_icon.svg" alt="" class="lazy"></a></li>
	                        <li><a href="#0"><img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="img/facebook_icon.svg" alt="" class="lazy"></a></li>
	                        <li><a href="#0"><img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="img/instagram_icon.svg" alt="" class="lazy"></a></li>
	                        <li><a href="#0"><img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="img/youtube_icon.svg" alt="" class="lazy"></a></li>
	                    </ul>
	                </div>
	            </div>
	        </div>
	        <p class="text-center"></p>
	    </div>
	  </footer>
  </div>  
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
      
    }
  },

  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },

  mounted() {
    this.cart = this.$store.state.cart
  },

  computed: {
    cartTotalLength(){
      let totalLength = 0

      for (let i =  0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      
      return totalLength
    }

  },
}
</script>


<style lang="scss">
  @import '../node_modules/bulma';

nav a {
  text-decoration:none !important;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block; 
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

</style>

<style>
.badge {
  padding-left: 9px;
  padding-right: 9px;
  -webkit-border-radius: 9px;
  -moz-border-radius: 9px;
  border-radius: 50%;
}

.label-warning[href],
.badge-warning[href] {
  background-color: #c67605;
}
#lblCartCount {
    font-size: 12px;
    background: red;
    color: #fff;
    padding: 0 5px;
    vertical-align: top;
    margin-left: -10px; 
}
</style>