import React from "react";
import Logo from "../images/green-rvz.png";
import { NavLink, Link } from "react-router-dom";
function Header() {
  return (
    <div className="header">
      <Link to="/">
        <img alt="logo" width="109" src={Logo} />
      </Link>
      <NavLink className="login" to="/signin">
        Sign in
      </NavLink>
    </div>
  );
}

export default Header;
