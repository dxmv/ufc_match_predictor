import { useState } from 'react';
import { FaSearch } from 'react-icons/fa';

interface SearchBarProps {
    onSearch: (query: string) => void;
    placeholder?: string;
}

const SearchBar: React.FC<SearchBarProps> = ({ onSearch, placeholder = "Search..." }) => {
    const [searchQuery, setSearchQuery] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSearch(searchQuery);
    };

    return (
        <form onSubmit={handleSubmit} className="w-full max-w-md mx-auto mb-6">
            <div className="relative flex items-center">
                <input
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    placeholder={placeholder}
                    className="w-full px-4 py-2 pl-10 text-gray-700 bg-white border border-gray-200 
                             rounded-lg focus:outline-none focus:border-blue-500 focus:ring-1 
                             focus:ring-blue-500 transition-colors"
                />
                <FaSearch className="absolute left-3 text-gray-400" />
                <button
                    type="submit"
                    className="absolute right-2 px-4 py-1 text-sm text-white bg-blue-500 
                             rounded-md hover:bg-blue-600 transition-colors"
                >
                    Search
                </button>
            </div>
        </form>
    );
};

export default SearchBar;