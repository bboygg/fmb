import React from 'react';
import Link from 'next/link';

export default function Nav() {
  return (
    <nav style={{ backgroundColor: 'grey', padding: '1rem' }}>
      <ul style={{ listStyle: 'none', display: 'flex', justifyContent: 'center', gap: '1rem' }}>
        <li>
          <Link href="/">Home</Link>
        </li>
        <li>
          <Link href="/battles">Battles</Link>
        </li>
        <li>
          <Link href="/about">About</Link>
        </li>
      </ul>
    </nav>
  );
}
