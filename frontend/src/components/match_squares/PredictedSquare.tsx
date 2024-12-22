const PredictedSquare = ({ blue, correct }: { blue?: boolean, correct: boolean }) => {
    return (
        <div className={`absolute top-0 ${correct ? (blue ? 'right-12' : 'left-12') : (blue ? 'right-0' : 'left-0')} w-10 h-10 bg-blue-500 rounded-md flex items-center justify-center text-white font-bold`}>
            W
        </div>
    );
};

export default PredictedSquare;