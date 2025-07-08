import React from "react";

function Button({ label, onClick, className = "", type = "button", alt = "" }) {
  return (
    <button
      onClick={onClick}
      type={type}
      aria-label={alt || label}
      className={`text-white px-6 py-3 rounded-md transition duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 ${className}`}
      style={{
        backgroundColor: "var(--color-brick-red)",
        color: "var(--color-white)",
      }}
    >
      {label}
    </button>
  );
}

export default Button;
