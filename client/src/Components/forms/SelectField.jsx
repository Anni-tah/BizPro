import React from 'react';
const SelectField = ({ name, label, options, register, error }) => {
    return (
      <div className="mb-4">
        <label className="block text-[#2d2d2d] mb-2">{label}</label>
        <select
          {...register(name)}
          className={`w-full p-2 px-4 border rounded bg-white text-[#2d2d2d] focus:outline-none focus:border-[#b8723e] ${
            error ? 'border-red-500' : 'border-[#525333]'
          }`}
        >
          <option value="">Select a {label.toLowerCase()}</option>
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        {error && <p className="text-red-500 text-sm">{error.message}</p>}
      </div>
    );
  };
  
  export default SelectField;
  