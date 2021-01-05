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
        <Link style={navStyle} to="/location">
          <li>Location</li>
        </Link>
        {/* <Link style={navStyle} to="/users">
          <li>Profile</li>
        </Link>
        <Link style={navStyle} to="/login">
          <li>Login</li>
        </Link>
        <Link style={navStyle} to="/registration">
          <li>Register</li>
        </Link> */}
      </ul>
    </nav>
  );
}

export default Nav;