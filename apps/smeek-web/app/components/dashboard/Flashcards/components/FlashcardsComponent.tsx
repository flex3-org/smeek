import React, { useState } from "react";
import { Carousel } from "primereact/carousel";

interface FlashcardItem {
  title: string;
  description: string;
}

interface FlashcardItemProps {
  flashcards: FlashcardItem[];
}

const FlashcardsComponent: React.FC<FlashcardItemProps> = ({ flashcards }) => {
  const [isFocusMode, setIsFocusMode] = useState(false);

  const handleToggle = () => {
    setIsFocusMode(!isFocusMode);
  };

  const responsiveOptions = [
    {
      breakpoint: "1400px",
      numVisible: 2,
      numScroll: 1,
    },
    {
      breakpoint: "1199px",
      numVisible: 3,
      numScroll: 1,
    },
    {
      breakpoint: "767px",
      numVisible: 2,
      numScroll: 1,
    },
    {
      breakpoint: "575px",
      numVisible: 1,
      numScroll: 1,
    },
  ];

  return (
    <>
      <div className="flex items-center justify-center my-4">
        <label className="switch">
          <input
            type="checkbox"
            id="togBtn"
            checked={isFocusMode}
            onChange={handleToggle}
          />
          <div className="slider round">
            <span className="on -ml-3 text-sm">Focus</span>
            <span className="off ml-3 text-sm">Grid</span>
          </div>
        </label>
      </div>

      <div>
        {isFocusMode ? (
          <div className="px-32">
            <Carousel
              value={flashcards}
              numVisible={1}
              numScroll={1}
              responsiveOptions={responsiveOptions}
              itemTemplate={productTemplate}
              autoFocus
            />
          </div>
        ) : (
          <div className="grid md:grid-cols-3 grid-cols-1 gap-6 p-4 px-12">
            {flashcards.map((flashcard, index) => (
              <div
                key={index}
                className="bg-white rounded-lg shadow-lg p-6 transition-transform transform hover:scale-105"
              >
                <h1 className="text-xl font-bold text-gray-800 mb-2">
                  {flashcard.title}
                </h1>
                <p className="text-gray-600">{flashcard.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </>
  );
};

const productTemplate = (flashcard: FlashcardItem) => {
  return (
    <div className="bg-white rounded-lg p-6 mx-12">
      <h1 className="text-xl font-bold text-gray-800 mb-2">
        {flashcard.title}
      </h1>
      <p className="text-gray-600">{flashcard.description}</p>
    </div>
  );
};

export default FlashcardsComponent;
