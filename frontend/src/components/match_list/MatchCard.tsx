import { Match, Fighter } from "../../types/match_types";
import { useNavigate } from 'react-router-dom';
import WinnerSquare from "../match_squares/WinnerSquare";
import PredictedSquare from "../match_squares/PredictedSquare";

const MatchCard = ({ match, upcoming }: { match: Match, upcoming?: boolean }) => {
    const navigate = useNavigate();

    const handleCardClick = () => {
        
        navigate(`/match/${upcoming ? "upcoming/" : ""}${match.id}`); // Redirect to the match details page
    };


    return (
        <div 
            className={`flex flex-col items-center justify-between w-full p-6 border-b transition-colors cursor-pointer mt-4 ${!upcoming ? (match.predicted === match.winner ? 'bg-green-100 hover:bg-green-200' : 'bg-red-100 hover:bg-red-200'):'bg-gray-100 hover:bg-gray-300'}`} 
            onClick={handleCardClick}
        >
            <div className='flex items-center justify-around w-1/5 mb-2'>
                <div className='text-sm text-gray-500 text-red-500'>{match.red_odds ? match.red_odds : "-"}</div>
                <div className='text-sm font-semibold text-gray-700'>ODDS</div>
                <div className='text-sm text-gray-500 text-blue-500'>{match.blue_odds ? match.blue_odds : "-"}</div>
            </div>
            <div className='flex flex-row items-center justify-between w-full'>
                <FighterPart fighter={match.red_fighter} winner={match.winner === "Red"} predicted={match.predicted == "Red"} />
                <div className='text-xl font-bold w-1/3 flex justify-center items-center'>vs</div>
                <FighterPart fighter={match.blue_fighter} winner={match.winner === "Blue"} predicted={match.predicted == "Blue"} blue={true} />
            </div>
        </div>
    );
};

const FighterPart = ({ fighter, blue, winner, predicted }: { fighter: Fighter, blue?: boolean, winner?: boolean, predicted?: boolean }) => {
    return (
        <div className={`flex flex-col items-center justify-center relative w-1/3`}>
            <img src={fighter.image_link} alt={fighter.name} className='max-w-80 max-h-80' />
            <p className={`mt-5 text-lg font-bold ${blue ? 'text-blue-500 hover:text-blue-700' : 'text-red-500 hover:text-red-700'}`}>{fighter.name}</p>
            {winner && <WinnerSquare blue={blue} />}
            {predicted && <PredictedSquare blue={blue} correct={predicted === winner} />}
        </div>
    );
};

export default MatchCard;