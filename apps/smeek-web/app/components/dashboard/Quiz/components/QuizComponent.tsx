import React, { useState } from "react";
import { FaCheck, FaTimes } from "react-icons/fa";

interface QuizItem {
  question: string;
  options: string[];
  correct_answer: string;
}

interface QuizComponentProps {
  data: QuizItem[];
}

const QuizComponent: React.FC<QuizComponentProps> = ({ data }) => {
  const [selectedAnswers, setSelectedAnswers] = useState<{
    [key: number]: string;
  }>({});
  const [submitted, setSubmitted] = useState<boolean>(false);

  const handleOptionChange = (questionIndex: number, option: string) => {
    setSelectedAnswers({
      ...selectedAnswers,
      [questionIndex]: option,
    });
  };

  const handleSubmit = () => {
    setSubmitted(true);
  };

  const labels = ["A", "B", "C", "D"];

  return (
    <div className="max-w-3xl mx-auto p-4">
      {data.map((questionItem: QuizItem, index: number) => (
        <div key={index} className="mb-6">
          <p className="text-sm text-gray-400">Question {index + 1}</p>
          <h3 className="text-xl font-semibold mb-2 pt-4">
            {questionItem.question}
          </h3>
          <div className="pt-4">
            {questionItem.options.map((option, idx) => {
              const isCorrect = option === questionItem.correct_answer;
              const isSelected = selectedAnswers[index] === option;
              const optionStyle = submitted
                ? isCorrect
                  ? "bg-green-200 text-black"
                  : isSelected
                  ? "bg-red-200 text-black"
                  : "bg-white text-black"
                : isSelected
                ? "bg-[#EAF3FF] border-2 border-[#2D80F6] text-[#2D80F6] text-white"
                : "bg-white text-black";

              return (
                <label
                  key={idx}
                  className={`block p-3 border rounded mb-2 cursor-pointer flex items-center ${optionStyle}`}
                >
                  <input
                    type="radio"
                    name={`question-${index}`}
                    value={option}
                    checked={isSelected}
                    onChange={() => handleOptionChange(index, option)}
                    className="hidden"
                    required
                  />
                  <span
                    className={`inline-flex items-center justify-center w-8 h-8 rounded-full mr-2 ${
                      submitted
                        ? (isCorrect && isSelected) || isCorrect
                          ? "bg-green-700 text-white"
                          : !isCorrect && isSelected
                          ? "bg-red-700 text-white"
                          : "bg-gray-100 text-black"
                        : isSelected
                        ? "bg-[#2D80F6] border-2 border-[#2D80F6] text-white"
                        : "bg-gray-100 text-black"
                    }`}
                  >
                    {submitted && isSelected ? (
                      isCorrect ? (
                        <FaCheck className="text-white" />
                      ) : (
                        <FaTimes className="text-white" />
                      )
                    ) : (
                      labels[idx]
                    )}
                  </span>
                  <span className="flex-1 text-black">{option}</span>
                </label>
              );
            })}
          </div>
        </div>
      ))}

      {data && (
        <>
          <button
            onClick={handleSubmit}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Submit
          </button>
        </>
      )}

      {submitted && (
        <div className="mt-4">
          <h3 className="text-2xl font-bold">Results:</h3>
          <ul>
            {data.map((questionItem: QuizItem, index: number) => (
              <li key={index} className="mt-2">
                {selectedAnswers[index] === questionItem.correct_answer ? (
                  <span className="text-green-500">
                    Question {index + 1}: Correct
                  </span>
                ) : (
                  <span className="text-red-500">
                    Question {index + 1}: Incorrect
                  </span>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default QuizComponent;
