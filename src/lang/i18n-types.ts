export interface Translation {
    // Hier erlauben wir JEDEN Text-Schlüssel, damit TS nicht meckert, 
    // wenn du neue Texte in deine JSON/TS Dateien einfügst.
    [key: string]: string; 
}