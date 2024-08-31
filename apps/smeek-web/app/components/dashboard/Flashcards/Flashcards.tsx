import { flashcards } from "@/utils/data";

export default function Flashcards() {
  return (
    <>
    <div className="flex items-center justify-center">
      <label className="switch">
        <input type="checkbox" id="togBtn" />
        <div className="slider round">
          <span className="on -ml-3 text-sm">Focus</span>
          <span className="off ml-3 text-sm">Grid</span>
        </div>
      </label>
      </div>
      <div>
        <div className="grid md:grid-cols-3 grid-cols-1 gap-6 p-4 px-12">
          {flashcards.map((flashcard) => (
            <div className="bg-white rounded-lg shadow-lg p-6 transition-transform transform hover:scale-105">
              <h1 className="text-xl font-bold text-gray-800 mb-2">{flashcard.title}</h1>
              <p className="text-gray-600">{flashcard.description}</p>
            </div>
          ))}
        </div>
      </div>
    </>
  )
}
