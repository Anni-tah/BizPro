import React from "react";
import { Link } from "react-router-dom";

function NavItem({ to, icon, label, onClick, className = "" }) {
  return (
    <li>
      <Link
        to={to}
        onClick={onClick}
        className={`flex items-center space-x-2 p-2 rounded hover:bg-gray-100 ${className}`}
      >
        {icon}
        <span>{label}</span>
      </Link>
    </li>
  );
}

export default NavItem;
