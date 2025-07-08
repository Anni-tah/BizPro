import { useState } from "react";
import React from "react";

const PasswordField = ({ register, errors={},name,label, placeholder }) => {
    const [showPassword, setShowPassword] = useState(false);
    
    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };
    
    return (
        <div className="mb-4">
        <label className="block text-dark mb-2">{label}</label>
        <div className="relative">
            <input
            type={showPassword ? "text" : "password"}
            {...register(name)}
            placeholder={placeholder}
            className={`w-full p-2 px-4 border rounded focus:outline-none focus:border-primary ${
                errors.name? "border-red-500" : "border-dark"
            }`}
            />
            <button
            type="button"
            onClick={togglePasswordVisibility}
            className="absolute right-2 top-1/2 transform -translate-y-1/2 text-dark"
            >
            {showPassword ? "Hide" : "Show"}
            </button>
        </div>
        {errors[name] && (
            <p className="text-red-500 text-sm">{errors.password.message}</p>
        )}
        </div>
    );
    }
export default PasswordField;