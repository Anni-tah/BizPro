import React, { useState } from "react";
import NavItem from "./NavItem";
import navItems from "./NavItems";
import { Menu, X } from "lucide-react";

function MobileMenu() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="md:hidden">
      <button onClick={() => setIsOpen(!isOpen)} aria-label="Toggle menu">
        {isOpen ? <X /> : <Menu />}
      </button>

      {isOpen && (
        <ul className="mt-2 space-y-2 bg-white rounded shadow p-2">
          {navItems.map((item) => (
            <NavItem
              key={item.label}
              to={item.to}
              icon={item.icon}
              label={item.label}
              onClick={() => setIsOpen(false)}
            />
          ))}
        </ul>
      )}
    </div>
  );
}

export default MobileMenu;
