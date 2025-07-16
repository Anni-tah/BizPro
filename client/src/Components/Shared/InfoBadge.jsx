const InfoBadge = ({ status }) => {
    const base = "px-2 py-1 rounded text-xs font-medium";
  
    const statusClasses = {
      Paid: "bg-green-100 text-green-700",
      Pending: "bg-yellow-100 text-yellow-700",
      Cancelled: "bg-red-100 text-red-700",
      Delivered: "bg-blue-100 text-blue-700",
    };
  
    const color = statusClasses[status] || "bg-gray-100 text-gray-700";
  
    return <span className={`${base} ${color}`}>{status}</span>;
  };
  
  export default InfoBadge;
  