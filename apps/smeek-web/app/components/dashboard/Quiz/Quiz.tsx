import { FaSearch } from "react-icons/fa";
import { useState } from "react";
import QuizComponent from "./components/QuizComponent";
import { quizData } from "@/utils/data";

interface QuizItem {
  question: string;
  options: string[];
  correct_answer: string;
}

export default function Quiz() {
  const [loading, setLoading] = useState<boolean>(false);
  const [quiz, setQuiz] = useState<QuizItem[]>([]);

  const generateQuiz = async (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    setLoading(true);
    try {
      // Uncomment and adjust axios request when needed
      // const res = await axios.get<QuizItem[]>("http://127.0.0.1:8000/quizdata");
      const fetchedData = quizData; // Replace with the actual fetched data
      setQuiz(fetchedData);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col justify-center items-center gap-6">
      <div className="flex items-center gap-8">
        <input type="file" className="bg-gray-300 p-2 rounded-md" />
        <button
          className="bg-[#333333] px-6 py-1 text-white rounded-md flex items-center gap-1"
          onClick={generateQuiz}
        >
          Generate Quiz <FaSearch size={16} />
        </button>
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : quiz.length > 0 ? (
        <QuizComponent data={quiz} />
      ) : null}
    </div>
  );
}
