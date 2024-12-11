import { Match, Fighter } from "../../types/match_types";
import { useNavigate } from 'react-router-dom';
import WinnerSquare from "../WinnerSquare";

const MatchCard = ({ match }: { match: Match }) => {
    const navigate = useNavigate();

    const handleCardClick = () => {
        navigate(`/match/${match.id}`); // Redirect to the match details page
    };

    console.log(match.winner,match.red_fighter.name,match.blue_fighter.name);

    return (
        <div 
            className='mt-10 flex flex-col items-center justify-between w-full p-6 border-b hover:bg-gray-100 transition-colors cursor-pointer' 
            onClick={handleCardClick}
        >
            <div className='flex items-center justify-around w-1/5 mb-2'>
                <div className='text-sm text-gray-500 text-red-500'>{match.red_odds}</div>
                <div className='text-sm font-semibold text-gray-700'>ODDS</div>
                <div className='text-sm text-gray-500 text-blue-500'>{match.blue_odds}</div>
            </div>
            <div className='flex flex-row items-center justify-between w-full'>
                <FighterPart fighter={match.red_fighter} winner={match.winner === "Red"}/>
                <div className='text-xl font-bold'>vs</div>
                <FighterPart fighter={match.blue_fighter} winner={match.winner === "Blue"} blue={true} />
            </div>
        </div>
    );
};

const FighterPart = ({ fighter, blue, winner }: { fighter: Fighter, blue?: boolean, winner?: boolean }) => {
    return (
        <div className={`flex flex-row items-center relative ${blue ? 'flex-row-reverse' : ''}`}>
            <img src={"https://dmxg5wxfqgb4u.cloudfront.net/2024-11/JONES_JON_BELT_11-16.png"} alt={fighter.name} className='max-w-80 max-h-80' />
            <div className='ml-4 text-lg font-bold'>{fighter.name}</div>
            {winner && <WinnerSquare blue={blue} />}
        </div>
    );
};

export default MatchCard;