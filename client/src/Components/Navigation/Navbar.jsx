import React from "react";
import { Link } from "react-router-dom";
import NavMenu from "./NavMenu";
import MobileMenu from "./MobileMenu";

function Navbar(){
    return(
    <nav className="bg-white shadow-md p-4">
        <div className="container mx-auto flex justify-between items-center">
       {/*logo*/}
       <Link to="/" className="flex items-center space-x-2">
       <div className="rounded-full bg-blue-600 w-6 h-6 flex items-center justify-center text-white font-bold">B</div>
       <span className="font-bold text-lg text-black">BizPro</span>
       </Link>
       {/*Desktop menu */}
       <NavMenu />

       {/*Mobile menu*/}
       <MobileMenu />
       </div>
    </nav>

    )
 

}
export default Navbar;