import { Match, Fighter } from "../../types/match_types";
import { useNavigate } from 'react-router-dom';

const MatchCard = ({ match }: { match: Match }) => {
    const navigate = useNavigate();

    const handleCardClick = () => {
        navigate(`/match/${match.id}`); // Redirect to the match details page
    };

    return (
        <div 
            className='mt-10 flex flex-col items-center justify-between w-full p-6 border-b hover:bg-gray-100 transition-colors cursor-pointer' 
            onClick={handleCardClick}
        >
            <div className='flex items-center justify-between w-full mb-2'>
                <div className='text-sm text-gray-500'>{match.red_odds}</div>
                <div className='text-sm font-semibold text-gray-700'>ODDS</div>
                <div className='text-sm text-gray-500'>{match.blue_odds}</div>
            </div>
            <div className='flex flex-row items-center justify-between w-full'>
                <FighterPart fighter={match.red_fighter} />
                <div className='text-xl font-bold'>vs</div>
                <FighterPart fighter={match.blue_fighter} blue={true} />
            </div>
        </div>
    );
};

const FighterPart = ({ fighter, blue }: { fighter: Fighter, blue?: boolean }) => {
    return (
        <div className={`flex flex-row items-center ${blue ? 'flex-row-reverse' : ''}`}>
            <img src={"https://dmxg5wxfqgb4u.cloudfront.net/2024-11/JONES_JON_BELT_11-16.png"} alt={fighter.name} className='max-w-80 max-h-80' />
            <div className='ml-4 text-lg font-bold'>{fighter.name}</div>
        </div>
    );
};

export default MatchCard;