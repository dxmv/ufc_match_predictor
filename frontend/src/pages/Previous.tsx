import { FaClipboardList } from 'react-icons/fa'; // Changed icon for matches trained on
import MatchList from '../components/match_list/MatchList';
import { Match } from '../types/match_types';
import { useEffect, useState } from 'react';
import { fetchAccuracy, fetchPreviousMatches } from '../services/api/matchesApi';
import SearchBar from '../components/SearchBar';

const Previous: React.FC = () => {
    // store the previous matches
    const [matches, setMatches] = useState<Array<Match>>([]);
    const [page, setPage] = useState<number>(1); // State for pagination
    const [hasMore, setHasMore] = useState<boolean>(true); // State to track if more matches are available
    const [accuracy, setAccuracy] = useState<number>(0); // Accuracy of the model



    // get the previous matches
    useEffect(() => {
        const loadMatches = async () => {
            const data = await fetchPreviousMatches(page,10);
            setMatches(prevMatches => [...prevMatches, ...data]); // Append new matches to existing ones
            setHasMore(data.length > 0); // Check if more matches are available
        };
        // get the accuracy of the model
        const loadAccuracy = async () => {
            const accuracy = await fetchAccuracy();
            setAccuracy(accuracy);
        };
        loadMatches();
        loadAccuracy();
    }, [page]);

    const loadMoreMatches = () => {
        if (hasMore) {
            setPage(prevPage => prevPage + 1); // Increment page to load more matches
        }
    };

    const handleSearch = (query: string) => {
        
    };

    return (
        <div className="min-h-screen">
            {/* Official background image */}
            <div className="relative h-96 bg-cover bg-center mb-10" style={{ backgroundImage: `url(https://dmxg5wxfqgb4u.cloudfront.net/styles/background_image_xl/s3/2024-11/120724-ufc-310-pantoja-vs-asakura-EVENT-ART.jpg?h=d1cb525d&itok=XWZWovZk)` }}>
                {/* Black overlay */}
                <div className="absolute top-0 left-0 w-full h-full bg-black opacity-60 flex flex-col justify-center items-center">
                    <h1 className="text-white text-5xl font-bold mt-10">Model accuracy: {(accuracy * 100).toFixed(2)}%</h1>
                    {/* Date and Location in the same row with icons */}
                    <div className="flex items-center text-white text-lg mt-5">
                        <span className="mr-2">
                            <FaClipboardList /> {/* New icon for matches trained on */}
                        </span>
                        <span>Matches trained on: {matches.length}</span> 
                    </div>
                </div>
            </div>
            <SearchBar 
                onSearch={handleSearch}
                placeholder="Search events..."
            />
            <MatchList matches={matches} />
            {hasMore && (
                <div className="flex justify-center">
                    <button onClick={loadMoreMatches} className="mt-4 py-2 px-4 bg-blue-500 text-white rounded mb-10">
                        Load More Matches
                    </button>
                </div>
            )}
        </div>
    );
};

export default Previous;