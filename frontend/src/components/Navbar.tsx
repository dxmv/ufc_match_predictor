import React from 'react';
import { Link } from 'react-router-dom';

const Navbar: React.FC = () => {
    return (
        <nav className="bg-transparent shadow-lg fixed top-0 w-full z-10" >
            <ul className="container mx-auto px-4 py-3 flex items-center justify-between">
                <li><Link to="/" className="text-gray-300 hover:text-white transition-colors duration-200">Home</Link></li>
                <div className="flex space-x-8">
                    <li><Link to="/upcoming" className="text-gray-300 hover:text-white transition-colors duration-200">Upcoming</Link></li>
                    <li><Link to="/previous" className="text-gray-300 hover:text-white transition-colors duration-200">Previous</Link></li>
                </div>
            </ul>
        </nav>
    );
};

export default Navbar;