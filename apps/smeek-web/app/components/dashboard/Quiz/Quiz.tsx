import { FaSearch } from "react-icons/fa";
import { useState } from "react";
import QuizComponent from "./components/QuizComponent";
import { quizData } from "@/utils/data";
import axios from "axios";

interface QuizItem {
  question: string;
  options: string[];
  correct_answer: string;
}

export default function Quiz() {
  const [loading, setLoading] = useState<boolean>(false);
  const [quiz, setQuiz] = useState<QuizItem[]>([]);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const generateQuiz = async (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (!selectedFile) {
      alert("Please select a file first!");
      return;
    }

    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("file", selectedFile);

      const res = await axios.post<QuizItem[]>(
        "http://127.0.0.1:8000/quiz/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      const fetchedData = res.data; // assuming response data is QuizItem[]
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
        <input
          type="file"
          className="bg-gray-300 p-2 rounded-md"
          onChange={handleFileChange}
        />
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
