import React from "react";
const Features = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
            <h1 className="text-3xl font-bold mb-4">Features</h1>
            <p className="text-lg text-gray-700 mb-8">
                Discover the amazing features of our application that make your experience seamless and enjoyable.
            </p>
            <ul className="list-disc list-inside text-left max-w-md">
                <li>Feature 1: User-friendly interface</li>
                <li>Feature 2: Real-time notifications</li>
                <li>Feature 3: Secure data handling</li>
                <li>Feature 4: Customizable settings</li>
            </ul>
        </div>
    );
}
export default Features;