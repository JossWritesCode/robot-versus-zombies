import React from "react";
import Logo from "../images/green-rvz.png";

function Header() {
  return (
    <div className="header">
      <img width="109" src={Logo} alt="RVZ" />
      <a className="login" href="#">
        Login
      </a>
    </div>
  );
}

export default Header;
