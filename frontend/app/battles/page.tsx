import React from 'react';
import { Metadata } from 'next';
import Nav from '../components/nav';
import Layout from '../layout';

export const metadata: Metadata = {
  title: 'Battles'
};

export default async function Page() {
  return (
    <Layout>
        <Nav />
        <div>
            <h1>Battles</h1>
            <p> List of Battles goes here</p>
        </div>
    </Layout>
  );
}