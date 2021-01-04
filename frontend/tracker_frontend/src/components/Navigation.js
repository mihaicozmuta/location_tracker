import React from "react";
import { Link } from "react-router-dom";

function Nav() {
  const navStyle = {
    color: "white",
  };
  return (
    <nav>
      <Link style={navStyle} to="/">
        <h3>Home</h3>
      </Link>

      <ul className="links-nav">
        <Link style={navStyle} to="/about">
          <li>About us</li>
        </Link>
        <Link style={navStyle} to="/users">
          <li>Profile</li>
        </Link>
        <Link style={navStyle} to="/login">
          <li>Login</li>
        </Link>
      </ul>
    </nav>
  );
}

export default Nav;