<?php

namespace App\Http\Controllers;

use App\Models\Article;
use Illuminate\Http\Request;

class ArticleController extends Controller
{
    public function index()
    {
        return response()->json(Article::orderBy('id', 'desc')->get());
    }

    public function show($id)
    {
        return response()->json(Article::find($id));
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'title' => 'required|string',
            'original_content' => 'required|string',
            'source_url' => 'required|url',
        ]);

        $article = Article::create($validated);
        return response()->json($article, 201);
    }

    public function update(Request $request, $id)
    {
        $article = Article::findOrFail($id);
        
        $article->update([
            'updated_content' => $request->updated_content,
            'references' => $request->references
        ]);

        return response()->json($article, 200);
    }
}