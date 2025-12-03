import React from "react";
import { Search } from "react-feather";

const Header = () => {
  return (
    <header>
      <div className="logo-search">
        <img src="/utensils.png" alt="Logo" className="logo" />
        <div className="search">
          <label className="visually-hidden" htmlFor="search">
            Search
          </label>
          <input type="text" placeholder="Search" id="search" />
          <Search />
        </div>
      </div>
      <h1>My Favorite Recipes</h1>
    </header>
  );
};

export default Header;