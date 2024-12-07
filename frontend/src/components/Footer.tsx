import React from 'react';
import { Link } from 'react-router-dom';
// import logo from '../path/to/logo.png'; // Adjust the path to your logo

const Footer: React.FC = () => {
    return (
        <footer className="bg-gray-900 shadow-lg">
            <div className="container mx-auto px-4 py-6 grid grid-cols-1 md:grid-cols-4 gap-6 h-full">
                <div className="flex flex-col items-between h-full">
                    {/* <img src={logo} alt="UFC Fight Predictor Logo" className="mb-4 w-24 h-24" /> */}
                    <p className="text-gray-400 mb-6">Get data-driven predictions for upcoming UFC fights.</p>
                    <p className="text-gray-400">© 2024 Your Company, LLC</p>
                </div>
                <div className="border-l border-gray-600 pl-4">
                    <h4 className="text-gray-300 font-semibold">Contact</h4>
                    <p className="text-gray-400 mt-1">Email: contact@yourcompany.com</p>
                    <p className="text-gray-400">Phone: (123) 456-7890</p>
                </div>
                <div className="border-l border-gray-600 pl-4">
                    <h4 className="text-gray-300 font-semibold">About</h4>
                    <p className="text-gray-400">Learn more about our mission and values.</p>
                </div>
                <div className="flex flex-col border-l border-gray-600 pl-4">
                    <h4 className="text-gray-300 font-semibold">Links</h4>
                    <div className="flex flex-col space-y-2 mt-1">
                        <Link to="/" className="text-gray-300 hover:text-white transition-colors duration-200">Home</Link>
                        <Link to="/upcoming" className="text-gray-300 hover:text-white transition-colors duration-200">Upcoming</Link>
                        <Link to="/previous" className="text-gray-300 hover:text-white transition-colors duration-200">Previous</Link>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;