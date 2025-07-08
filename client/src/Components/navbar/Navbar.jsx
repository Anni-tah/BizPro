import React, { useState } from "react";
import { FiMenu, FiX, FiHome, FiGrid, FiDollarSign, FiUser } from "react-icons/fi";
import { NavLink } from "react-router-dom";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const toggleMenu = () => setMenuOpen(!menuOpen);

  const navLinkClasses = ({ isActive }) =>
    `flex items-center space-x-1 cursor-pointer transition-colors duration-300 ease-in-out ${
      isActive ? "text-blue-700 font-semibold" : "text-gray-700 hover:text-blue-700"
    }`;

  return (
    <nav className="w-full bg-white shadow-md fixed top-0 left-0 z-50">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        {/* Logo section */}
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 rounded-full bg-blue-700 flex items-center justify-center">
            <div className="w-4 h-4 rounded-full bg-white"></div>
          </div>
          <span className="text-xl font-semibold text-blue-700">BizPro</span>
        </div>

        {/* Desktop Nav */}
        <ul className="hidden md:flex space-x-8 font-medium">
          <li>
            <NavLink to="/" className={navLinkClasses}>
              <FiHome />
              <span>Home</span>
            </NavLink>
          </li>
          <li>
            <NavLink to="/features" className={navLinkClasses}>
              <FiGrid />
              <span>Features</span>
            </NavLink>
          </li>
          <li>
            <NavLink to="/pricing" className={navLinkClasses}>
              <FiDollarSign />
              <span>Pricing</span>
            </NavLink>
          </li>
          <li>
            <NavLink to="/about" className={navLinkClasses}>
              <FiUser />
              <span>About</span>
            </NavLink>
          </li>
        </ul>

        {/* Hamburger icon */}
        <div className="md:hidden">
          <button onClick={toggleMenu} className="text-blue-700 text-2xl focus:outline-none">
            {menuOpen ? <FiX /> : <FiMenu />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      {menuOpen && (
        <ul className="md:hidden bg-white px-6 pb-4 space-y-4 font-medium">
          <li>
            <NavLink to="/" className={navLinkClasses}>
              <FiHome />
              <span>Home</span>
            </NavLink>
          </li>
          <li>
            <NavLink to="/features" className={navLinkClasses}>
              <FiGrid />
              <span>Features</span>
            </NavLink>
          </li>
          <li>
            <NavLink to="/pricing" className={navLinkClasses}>
              <FiDollarSign />
              <span>Pricing</span>
            </NavLink>
          </li>
          <li>
            <NavLink to="/about" className={navLinkClasses}>
              <FiUser />
              <span>About</span>
            </NavLink>
          </li>
        </ul>
      )}
    </nav>
  );
}

export default Navbar;
