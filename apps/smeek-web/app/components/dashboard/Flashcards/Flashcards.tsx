import { FaSearch } from "react-icons/fa";
import { useState } from "react";
import FlashcardsComponent from "./components/FlashcardsComponent";
import axios from "axios";
import { flashcards } from "@/utils/data";

interface FlashcardItem {
  title: string;
  description: string;
}

export default function Flashcards() {
  const [loading, setLoading] = useState<boolean>(false);
  const [flashcards, setFlashcards] = useState<FlashcardItem[]>([]);
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

      const res = await axios.post<FlashcardItem[]>(
        "https://smeek3.jollydesert-73a8e64b.eastus.azurecontainerapps.io/flashcards",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      const fetchedData = res.data;
      setFlashcards(fetchedData);
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
          Generate Flashcards <FaSearch size={16} />
        </button>
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : flashcards.length > 0 ? (
        <FlashcardsComponent flashcards={flashcards} />
      ) : null}
    </div>
  );
}
