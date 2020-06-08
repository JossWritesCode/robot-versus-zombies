import React from "react";
import Logo from "../images/green-rvz.png";
import { NavLink } from "react-router-dom";
function Header() {
  return (
    <div className="header">
      <img width="109" src={Logo} alt="RVZ" />
      <NavLink className="login" to="/signin">
        Sign in
      </NavLink>
    </div>
  );
}

export default Header;
