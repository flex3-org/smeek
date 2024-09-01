import React, { useState } from "react";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";

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

  return (
    <>
      {/* <div className="flex items-center justify-center my-4">
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
      </div> */}

      <div>
        {/* {isFocusMode ? (
          <div className="mx-auto max-w-lg">
            <Carousel
              className="mx-auto max-w-xs"
              showThumbs={false}
              showStatus={false}
              centerMode={true}
              centerSlidePercentage={80}
            >
              {flashcards.map((flashcard, index) => (
                <div
                  key={index}
                  className="bg-white rounded-lg shadow-lg p-6 transition-transform transform hover:scale-105 border-2"
                >
                  <h1 className="text-xl font-bold text-gray-800 mb-2">
                    {flashcard.title}
                  </h1>
                  <p className="text-gray-600">{flashcard.description}</p>
                </div>
              ))}
            </Carousel>
          </div>
        ) : ( */}
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
        {/* )} */}
      </div>
    </>
  );
};

export default FlashcardsComponent;
