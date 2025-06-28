import React from "react";
import NavItems from "./NavItems";
import NavItem from "./NavItem";

  function NavMenu(){
    return(
        <ul className="hidden md:flex space-x-6 text-gray-600">
            {NavItems.map((item)=>
            <NavItem 
            key={item.label}
            to={item.to}
            icon={item.icon}
            label={item.label}
            className="hover:text-black"
            
            />
            )}

        </ul>
    )
  }
  export default NavMenu;