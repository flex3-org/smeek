import { IoIosSend } from "react-icons/io";
import axios from "axios";
import { useState } from "react";

interface Message {
  text: string;
  type: 'user' | 'bot';
}

export default function ChatSection() {
  const [userInput, setUserInput] = useState<string>("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false); // Add loading state

  const chat = async () => {
    try {
      setLoading(true); // Set loading to true when starting request
      const res = await axios.post<{ response: string }>('http://127.0.0.1:8000/chat', {
          user_input: userInput
      });

      setMessages(prevMessages => [
        ...prevMessages,
        { text: userInput, type: 'user' },
        { text: res?.data?.response, type: 'bot' }
      ]);
      setUserInput(""); // Clear input field
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false); // Set loading to false when request is complete
    }
  };

  return (
    <div className="flex flex-col px-4 pt-20">
      <div className="flex-grow overflow-auto">
        <div className="space-y-4">
          {messages.map((msg, index) => (
            <div key={index} className={`flex ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`p-3 rounded-lg ${msg.type === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}>
                {msg.text}
              </div>
            </div>
          ))}
          {loading && (
            <div className="flex justify-center">
              <div className="animate-spin rounded-full border-t-2 border-blue-500 border-solid w-8 h-8"></div> {/* Spinner */}
            </div>
          )}
        </div>
      </div>
      <div className="mt-4">
        <div className="flex items-center gap-4">
          <input
            type="text"
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            className="p-3 bg-gray-300 rounded-full w-full focus:outline-none"
            placeholder="Message Smeek"
          />
          <button
            onClick={chat}
            className="bg-gray-300 p-2 inline-flex items-center justify-center w-12 h-12 rounded-full"
          >
            <IoIosSend className="text-2xl" />
          </button>
        </div>
      </div>
    </div>
  );
}
