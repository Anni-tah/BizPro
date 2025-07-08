import React from "react";
import { FiFacebook, FiTwitter, FiLinkedin } from "react-icons/fi";

const Footer = () => {
  return (
    <footer className="bg-gray-100 text-gray-700 py-10 px-4">
      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 rounded-full bg-blue-700 flex items-center justify-center">
            <div className="w-4 h-4 rounded-full bg-white"></div>
          </div>
          <span className="text-xl font-semibold text-blue-700">BizPro</span>
        </div>

        {/* Navigation Links */}
        <ul className="flex justify-center space-x-6 text-sm font-medium">
          <li><a href="/features" className="hover:text-blue-700 transition">Features</a></li>
          <li><a href="/pricing" className="hover:text-blue-700 transition">Pricing</a></li>
          <li><a href="/about" className="hover:text-blue-700 transition">About</a></li>
          <li><a href="/contact" className="hover:text-blue-700 transition">Contact</a></li>
        </ul>

        {/* Social Media Icons */}
        <div className="flex justify-end space-x-4 text-xl text-gray-600">
          <a href="#" className="hover:text-blue-700 transition"><FiFacebook /></a>
          <a href="#" className="hover:text-blue-700 transition"><FiTwitter /></a>
          <a href="#" className="hover:text-blue-700 transition"><FiLinkedin /></a>
        </div>
      </div>

      {/* Bottom */}
      <div className="text-center text-xs mt-10 text-gray-500">
        © {new Date().getFullYear()} BizPro. All rights reserved.
      </div>
    </footer>
  );
};

export default Footer;
