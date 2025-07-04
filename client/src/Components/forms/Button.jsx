const Button = ({ type, children, className, onClick, disabled }) => {
    return (
        <button
            type={type}
            onClick={onClick}
            disabled={disabled}
            className={`w-full p-2 px-4 bg-[#525333] text-white mt-4 hover:bg-[#b8723e] 
                focus:outline-none focus:ring-2 focus:ring-[#cf8852] ${className} ${
                disabled ? "opacity-50 cursor-not-allowed" : ""
            }`}
        >
            {children}
        </button>
    );
}
export default Button;