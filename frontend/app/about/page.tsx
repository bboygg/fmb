import React from 'react';
import Layout from '../layout';
import { Metadata } from 'next';
import Nav from '../components/nav';

export const metadata: Metadata = {
  title: 'About'
};

export default async function Page() {
    return (
        <Layout>
            <Nav />
            <div>
                <h1>About Us</h1>
                <p> George, Vorleak 코딩 중 ...</p>
            </div>
        </Layout>
    );
}