const InputField = ({ label, name, type = "text", placeholder, register, error }) => {
    return (
      <div className="mb-4">
        <label className="block text-[#2d2d2d] mb-2">{label}</label>
        <input
          type={type}
          placeholder={placeholder}
          {...register(name)}
          className={`w-full p-2 px-4 border rounded focus:outline-none ${
            error ? 'border-red-500' : 'border-[#525333]'
          }`}
        />
        {error && <p className="text-red-500 text-sm">{error.message}</p>}
      </div>
    );
  };
  
  export default InputField;
  