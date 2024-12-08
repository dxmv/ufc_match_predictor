import { FaClipboardList } from 'react-icons/fa'; // Changed icon for matches trained on
import MatchList from '../components/match_list/MatchList';
import { Match } from '../types/match_types';
import { useEffect, useState } from 'react';
import { fetchPreviousMatches } from '../services/api/matchesApi';


const Previous: React.FC = () => {
    // store the previous matches
    const [matches, setMatches] = useState<Array<Match>>([]);

    // get the previous matches
    useEffect(() => {
        const loadMatches = async () => {
            const data = await fetchPreviousMatches();
            setMatches(data);
        };
        loadMatches();
    }, []);

    console.log(matches);

    return (
        <div className="min-h-screen">
            {/* Official background image */}
            <div className="relative h-96 bg-cover bg-center" style={{ backgroundImage: `url(https://dmxg5wxfqgb4u.cloudfront.net/styles/background_image_xl/s3/2024-11/120724-ufc-310-pantoja-vs-asakura-EVENT-ART.jpg?h=d1cb525d&itok=XWZWovZk)` }}>
                {/* Black overlay */}
                <div className="absolute top-0 left-0 w-full h-full bg-black opacity-60 flex flex-col justify-center items-center">
                    <h1 className="text-white text-5xl font-bold mt-10">Model accuracy: 67%</h1>
                    {/* Date and Location in the same row with icons */}
                    <div className="flex items-center text-white text-lg mt-5">
                        <span className="mr-2">
                            <FaClipboardList /> {/* New icon for matches trained on */}
                        </span>
                        <span>Matches trained on: 100</span> 
                    </div>
                </div>
            </div>
            <MatchList matches={matches} />
        </div>
    );
};

export default Previous;