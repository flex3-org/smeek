import Link from "next/link";
import Image from "next/image";
import smeek from "../../public/logo.png";

export default function Navbar() {
  return (
    <>
      <div className="flex items-center justify-between md:px-20 px-4 py-6">
        <div className="flex items-center gap-1">
          <Image width={50} height={50} src={smeek} alt="logo" />
          <p className="text-2xl font-bold">smeek</p>
        </div>
        <div className="flex items-center gap-8 0">
          <p className="hidden md:block">Features</p>
          <Link
            href="/dashboard"
            className="py-2 px-4 bg-blue-500 text-white rounded-full"
          >
            Try for free
          </Link>
        </div>
      </div>
    </>
  );
}
