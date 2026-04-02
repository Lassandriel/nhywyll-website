import { de } from './de';
import { en } from './en';
import type { Translation } from './i18n-types'; // Hier das 'type' ergänzen

export const translations: { [key: string]: Translation } = {
    de: de,
    en: en
};