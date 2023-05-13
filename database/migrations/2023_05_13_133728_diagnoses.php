<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('diagnoses', function (Blueprint $table) {
            $table->id();

            $table->string('name');
            $table->text('treatment_plan');
            $table->boolean('active');
            $table->date('ended_at');


            $table->unsignedBigInteger('medical_record_id');

            $table->foreign('medical_record_id')->references('id')->on('medical_records');


            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('diagnoses');
    }
};
