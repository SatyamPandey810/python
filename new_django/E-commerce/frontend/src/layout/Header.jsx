import React from 'react'
import { Link } from 'react-router-dom'

export default function Header() {
  return (
    <header class="header">
      <div class="container-fluid">
        <div class="row">
          <div class="col-xl-3 col-lg-2">
            <div class="header__logo">
              <a href="./index.html"><img src="img/logo.png" alt="" /></a>
            </div>
          </div>
          <div class="col-xl-6 col-lg-7">
            <nav class="header__menu">
              <ul>
                <li class="active"><Link to="/">Home</Link></li>
                <li><a href="#">Women’s</a></li>
                <li><a href="#">Men’s</a></li>
                <li><a href="./shop.html">Shop</a></li>
                <li><a href="#">Pages</a>
                  <ul class="dropdown">
                    <li><a href="./product-details.html">Product Details</a></li>
                    <li><a href="./shop-cart.html">Shop Cart</a></li>
                    <li><a href="./checkout.html">Checkout</a></li>
                    <li><Link to="/blog">Blog Details</Link></li>
                  </ul>
                </li>
                <li><Link to="/blog">Blog</Link></li>
                <li><Link to="/contact">Contact</Link></li>
              </ul>
            </nav>
          </div>
          <div class="col-lg-3">
            <div class="header__right">
              <div class="header__right__auth">
                <a href="#">Login</a>
                <a href="#">Register</a>
              </div>
              <ul class="header__right__widget">
                <li><span class="icon_search search-switch"></span></li>
                <li><a href="#"><span class="icon_heart_alt"></span>
                  <div class="tip">2</div>
                </a></li>
                <li><a href="#"><span class="icon_bag_alt"></span>
                  <div class="tip">2</div>
                </a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="canvas__open">
          <i class="fa fa-bars"></i>
        </div>
      </div>
    </header>
  )
}
