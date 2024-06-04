/**
 * This file defines an Interceptor using axios. The Interceptor will automatically add
 * the correct headers, such as an access token, to all network requests. This eliminates
 * the need to manually write headers multiple times in the code, ensuring that every request
 * has the necessary headers for proper communication.
 */

import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

const apiUrl = '/choreo-apis/awbo/backend/rest-api-be2/v1.0';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
        ? import.meta.env.VITE_API_URL
        : apiUrl,
});

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;