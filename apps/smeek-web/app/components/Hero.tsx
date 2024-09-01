"use client";
import { motion } from "framer-motion";
import { Highlight } from "./ui/hero-highlight";
import Link from "next/link";
import Image from "next/image";
import video from "../../public/smeek_demo.gif";

export function Hero() {
  return (
    <>
      <div className="flex flex-col items-center justify-center md:pt-12 pt-8 md:px-4 px-12">
        <motion.h1
          initial={{
            opacity: 0,
            y: 20,
          }}
          animate={{
            opacity: 1,
            y: [20, -5, 0],
          }}
          transition={{
            duration: 0.5,
            ease: [0.4, 0.0, 0.2, 1],
          }}
          className="text-2xl md:text-4xl lg:text-5xl font-bold text-neutral-700 max-w-4xl leading-relaxed lg:leading-snug text-center mx-auto"
        >
          Your Personal AI{" "}
          <Highlight className="text-black dark:text-white">mentor!</Highlight>
        </motion.h1>
        <p className="md:text-xl text-center text-gray-400 pt-3">
          This will help you study, learn, and maintain consistency
        </p>
        <Link
          href="/dashboard"
          className="py-2 px-4 bg-blue-500 text-white rounded-full mt-4"
        >
          Try for free
        </Link>
        <div className="pt-8">
          <Image
            src={video}
            width={1000}
            height={400}
            alt="video"
            className="rounded-lg shadow-2xl"
          />
        </div>
      </div>
    </>
  );
}
